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
        tbl.column('valori_correnti', dtype='X', name_long='Valori Correnti')
            #BAG con una riga per misura
    
    def counter_codice(self,record=None):
        return dict(format='$NNNNNN',showOnLoad=True,code='*')

    

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
        for misura in misure:
            segno = random.choice([-1,1])
            valore_corrente_misura = valori_correnti[misura['id']]
            if not valore_corrente_misura:
                valore_corrente_misura = random.choice(drange(misura['valore_minimo'],
                                                    misura['valore_massimo'], 
                                                    misura['step']))

            n_intervalli = int((misura['valore_massimo']-misura['valore_minimo'])/misura['step'])
            step_corrente = int((valore_corrente_misura-misura['valore_minimo'])/n_intervalli)
            nuovo_step = random.choice(list(range(n_intervalli)))
            

            valore_nuovo = misura['valore_minimo']+(nuovo_step*misura['step'])
            record_rilevazione = tbl_rilevazioni.newrecord(componente_id=componente_id,
                        componente_tipo_misura_id=misura['id'],
                        valore=valore_nuovo,ts=ts)
            tbl_rilevazioni.insert(record_rilevazione)
            valori_correnti.setItem(misura['id'], valore_nuovo, dict(valore=valore_nuovo,valore_minimo=misura['valore_minimo'],
                                                                    valore_massimo=misura['valore_massimo'],
                                                                    valore_imposto=None))
        with self.recordToUpdate(pkey=componente_id) as record:
            record['valori_correnti']=valori_correnti
        if commit:
            self.db.commit()




    
