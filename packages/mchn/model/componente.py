#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrdecorator import public_method
from decimal import Decimal
from datetime import datetime
from gnr.core.gnrbag import Bag
import random


class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('componente', pkey='id', name_long='!![it]Componente', 
                    name_plural='!![it]Componenti',caption_field='descrizione')
        self.sysFields(tbl,counter='struttura_id')
        tbl.column('codice',size=':6',name_long='Codice',unique=True)
        tbl.column('identificativo', size=':30', name_long='Identificativo')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('componente_tipo_id',size='22',name_long='Tipo').relation('componente_tipo.id',
                    relation_name='componenti',mode='foreignkey')
        tbl.column('dati_componente_tipo',dtype='X',name_long='!![it]Dati componente',subfields='componente_tipo_id')
        tbl.column('data_installazione','D',name_long='!![it]Data installazione')

        tbl.column('struttura_id',size='22', group='_', name_long='Struttura'
                    ).relation('componente_struttura.id', relation_name='componenti',
                                mode='foreignkey',onDelete='raise')
        tbl.column('ultima_rilevazione_id',size='22', group='_', name_long='Ultima rilevazione'
                    ).relation('componente_rilevazione.id',mode='foreignkey', onDelete='setnull',onDelete_sql='setnull')
        tbl.aliasColumn('valori_correnti','@ultima_rilevazione_id.rilevazioni')
    def counter_codice(self,record=None):
        return dict(format='$NNNNNN',showOnLoad=True,code='*')
    

    @public_method
    def popola_rilevazioni_componenti(self, componenti_pkeys=None, ts=None, commit=True):
        if not componenti_pkeys:
            componenti_pkeys = [r['id'] for r in self.query().fetch()]
        for componente_id in componenti_pkeys:
            self.popola_rilevazioni(componente_id=componente_id,ts=ts,commit=False)
        self.db.commit()

    @public_method
    def popola_rilevazioni(self, componente_id=None, ts=None, commit=True):
        def drange(start, stop, step):
            out = []
            r = start
            while r < stop:
                out.append(r)
                r += step
            return out
        ts = ts or datetime.now()
        componente_tipo_id,valori_correnti = self.readColumns(columns='$componente_tipo_id,$valori_correnti', pkey=componente_id)
        if valori_correnti:
            valori_correnti = Bag(valori_correnti)
        else:
            valori_correnti = Bag()
        tbl_misure = self.db.table('mchn.componente_tipo_misura')
        tbl_rilevazioni = self.db.table('mchn.componente_rilevazione')
        misure = tbl_misure.query("*,$valore_massimo,$valore_minimo,$step,$tipo_dato",
            where="$componente_tipo_id=:componente_tipo_id",
            componente_tipo_id=componente_tipo_id).fetch()
        #segno = random.choice([-1,1])
        rilevazioni = Bag()
        record_rilevazione = tbl_rilevazioni.newrecord(componente_id=componente_id,
                                                        ts=ts)
        for misura in misure:
            segno = random.choice([-1,1])
            valore_corrente_misura = 0
            if valori_correnti[misura['misura_codice']]:
                valore_corrente_misura = valori_correnti[misura['misura_codice']]['valore']
                if not valore_corrente_misura:
                    valore_corrente_misura = random.choice(drange(misura['valore_minimo'],
                                                        misura['valore_massimo'], 
                                                        misura['step']))
            n_intervalli = int((misura['valore_massimo']-misura['valore_minimo'])/misura['step'])
            step_corrente = int((valore_corrente_misura-misura['valore_minimo'])/n_intervalli)
            nuovo_step = random.choice(list(range(n_intervalli)))
            valore_nuovo = misura['valore_minimo']+(nuovo_step*misura['step'])
            rilevazioni[misura['misura_codice']] = Bag(dict(misura_codice=misura['misura_codice'],valore=valore_nuovo))
        record_rilevazione['rilevazioni'] = rilevazioni
        tbl_rilevazioni.insert(record_rilevazione)
        with self.recordToUpdate(pkey=componente_id) as record:
            record['ultima_rilevazione_id']=record_rilevazione['id']
        if commit:
            self.db.commit()



    
