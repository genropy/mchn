# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('componente_struttura_alias',pkey='id',
                    name_long='!!Alias per struttura',
                      name_plural='!!Alias per struttura')
        self.sysFields(tbl)
        tbl.column('struttura_id',size='22',group='_',
                    name_long='Struttura '
                    ).relation('componente_struttura.id',
                                 mode='foreignkey', 
                                 onDelete='cascade',
                                 relation_name='componenti_alias')
        tbl.column('componente_id',size='22',group='_',
                    name_long='Componente'
                    ).relation('componente.id',
                                 mode='foreignkey', 
                                    onDelete='cascade',
                                    relation_name='struttura_alias')
