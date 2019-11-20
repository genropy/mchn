#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='mchn package',sqlschema='mchn',sqlprefix=True,
                    name_short='Mchn', name_long='Mchn', name_full='Mchn')
                    
    def config_db(self, pkg):
        pass
    
    def custom_type_dec(self):
        return dict(dtype='N',size='12,2',format='#,###.00')

class Table(GnrDboTable):
    pass
