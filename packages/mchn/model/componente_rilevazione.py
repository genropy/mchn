
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_rilevazione', pkey='id', name_long='!!Rilevazione', name_plural='!!Rilevazioni',caption_field='ts')
        self.sysFields(tbl)
        tbl.column('componente_id', size='22').relation('componente.id', mode='foreignkey', relation_name='rilevazioni')
        tbl.column('componente_tipo_misura_id', size='22').relation('componente_tipo_misura.id', mode='foreignkey', relation_name='rilevazioni')
        tbl.column('ts', dtype='DH', name_long='!!Timestamp')
        tbl.column('valore', dtype='dec', name_long='!!Valore')
        