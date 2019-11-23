
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_rilevazione', pkey='id', name_long='!!Rilevazione', name_plural='!!Rilevazioni',caption_field='ts')
        self.sysFields(tbl)
        tbl.column('componente_id', size='22',name_long='Componente').relation('componente.id', mode='foreignkey', relation_name='rilevazioni')
        tbl.column('ts', dtype='DH', name_long='!!Timestamp')
        tbl.column('rilevazioni',dtype='X', name_long='!!Rilevazioni')
        
    def trigger_onInserted(self,record):
        self.allineaRigheRilevazione(record)

    def trigger_onUpdated(self,record,old_record=None):
        self.allineaRigheRilevazione(record)

    def allineaRigheRilevazione(self,record=None):
        rilevazione_riga = self.db.table('mchn.componente_rilevazione_riga')
        rilevazione_riga.sql_deleteSelection('$rilevazione_id=:rid',rid=record['id'])
        rilevazioni = record['rilevazioni']
        rilevazione_id = record['id']
        for v in rilevazioni.values():
            v['rilevazione_id'] = rilevazione_id
            rilevazione_riga.insert(v)
