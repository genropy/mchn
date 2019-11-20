# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_ubicazione', pkey='id', name_long='Ubicazione', 
                    name_plural='Ubicazione',caption_field='descrizione')
        self.sysFields(tbl,hierarchical='descrizione',
                        counter=True)
        tbl.column('descrizione', size=':40', name_long='Descrizione')
        