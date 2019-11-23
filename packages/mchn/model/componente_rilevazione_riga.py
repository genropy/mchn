
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_rilevazione_riga', pkey='id', name_long='!!Rilevazione', name_plural='!!Rilevazioni',caption_field='ts')
        self.sysFields(tbl,counter='rilevazione_id')
        tbl.column('rilevazione_id', size='22',
                    name_long='Rilevazione').relation('componente_rilevazione.id', mode='foreignkey', 
                                        relation_name='righe',onDelete='cascade')
        tbl.column('misura_codice',size=':20')
        tbl.column('valore', dtype='dec', name_long='!!Valore')
        