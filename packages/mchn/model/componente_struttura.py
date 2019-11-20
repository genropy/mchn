# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_struttura', pkey='id', name_long='Struttura', 
                    name_plural='Struttura',caption_field='descrizione')
        self.sysFields(tbl,hierarchical='descrizione',hierarchical_root_id=True,counter=True)
        tbl.column('descrizione', size=':40', name_long='Descrizione')
        tbl.column('geocoder', name_long='Geocoder', name_short='Geocoder')