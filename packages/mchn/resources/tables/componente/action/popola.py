
from gnr.web.batch.btcaction import BaseResourceAction
import time
from dateutil.rrule import rrule,MINUTELY
from datetime import datetime
from gnr.core.gnrbag import Bag


caption = 'Popola rilevazioni'
description='Popola rilevazioni'

class Main(BaseResourceAction):
    batch_prefix = 'PR'
    batch_title = 'Popola rilevazioni'
    batch_cancellable = True
    batch_immediate = True
    batch_delay = 0.5

    def do(self):
        selection = self.get_selection()
        if not selection:
            return
        tbl_componente = self.db.table('mchn.componente')
        print(self.batch_parameters)
        data_inizio = self.batch_parameters['data_inizio']
        ora_inizio = self.batch_parameters['ora_inizio']
        data_fine = self.batch_parameters['data_fine']
        ora_fine = self.batch_parameters['ora_fine']
        intervallo = self.batch_parameters['intervallo'] or 5
        if not data_inizio and data_fine and ora_inizio and data_fine:
            timestamps = [datetime.now()]
        else:
            ts_inizio = datetime.combine(data_inizio, ora_inizio)
            ts_fine = datetime.combine(data_fine, ora_fine)
            timestamps = rrule(MINUTELY,interval=intervallo,
                    dtstart=ts_inizio, until=ts_fine)
        for componente in self.btc.thermo_wrapper(selection,'componente',message=self.get_record_caption):
            for ts in timestamps:
                tbl_componente.popola_rilevazioni(componente_id=componente['pkey'], ts=ts, commit=False)
        self.db.commit()



    def table_script_parameters_pane(self,pane,**kwargs):
        pane.data('.intervallo',5)
        fb = pane.formbuilder(cols=2, border_spacing='5px',dragClass='draggedItem')
        fb.dateTextBox(value='^.data_inizio',lbl='Data Inizio')
        fb.timeTextBox(value='^.ora_inizio',lbl='Ora Inizio')
        fb.dateTextBox(value='^.data_fine',lbl='Data Fine')
        fb.timeTextBox(value='^.ora_fine',lbl='Ora Fine')
        fb.textBox(value='^.intervallo', lbl='Intervallo')
        