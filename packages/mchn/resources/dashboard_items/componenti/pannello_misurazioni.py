# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------
# Copyright (c) : 2004 - 2007 Softwell sas - Milano 
# Written by    : Giovanni Porcari, Michele Bertoldi
#                 Saverio Porcari, Francesco Porcari
#--------------------------------------------------------------------------
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 2.1 of the License, or (at your option) any later version.

#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#Lesser General Public License for more details.

#You should have received a copy of the GNU Lesser General Public
#License along with this library; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound
from gnr.core.gnrlist import sortByItem


try:
    from gnrpkg.biz.dashboard import BaseDashboardItem
except:
    BaseDashboardItem = object

caption = 'Pannello misurazioni'
description = 'Pannello misurazioni'
objtype = 'mchn_misurazioni'
table = 'mchn.componente_misurazione'

item_parameters = [dict(value='^.componente_id',lbl='Componente',tag='dbselect',
                        dbtable='mchn.componente',
                        validate_notnull=True),
                    dict(value='^.limit',lbl='Limite',tag='numberTextBox',width='5em',
                        default=100)]


class Main(BaseDashboardItem):
    py_requires='mchn_component:ComponenteMisurazioni'

    title_template = '$title'
    
    def content(self,pane,componente_id=None,**kwargs):
        bc = pane.borderContainer()
        bc.dataRpc('{}.struttura_rilevazione'.format(self.workpath),
                    self.db.table('mchn.componente_tipo').getStrutturaRipartizioni,
                    componente_id='^.conf.componente_id',
                    _fired='^{}.runItem'.format(self.workpath),
                    _onResult="""FIRE {}.structLoaded;""".format(self.workpath))
        th = bc.contentPane(region='left',width='50%',splitter=True
                ).plainTableHandler(datapath='{}.rilevazioni'.format(self.workpath),
                            table='mchn.componente_rilevazione',
                            viewResource='ViewFromComponente',
                            condition='$componente_id=:compid',
                            condition_compid='={}.conf.componente_id'.format(self.storepath),
                            view_store__doReload='^{}.structLoaded'.format(self.workpath),
                            view_structpath='{}.struttura_rilevazione'.format(self.workpath))
        th.view.store.attributes['limit'] = '^{}.conf.limit'.format(self.storepath)
        #bc.contentPane(region='center',overflow='hidden')
        center = bc.contentPane(region='center',overflow='hidden')
        center.dygraph(data='^{}.rilevazioni.view.store'.format(self.workpath),
                    options='^{}.conf.dygraph_options'.format(self.storepath),
                    columns='ts,rilevazioni_TF_IN_valore',
                    position='absolute',
                    top='0',bottom='0',left='0',right='0')

    def configuration(self,pane,componente_id=None,limit=None,**kwargs):
        bc = pane.borderContainer()
        pane.data('.componente_id',componente_id)
        pane.data('.limit',limit)
        pane.data('.dygraph_options.labels',['TS','TF IN'])
        #pane.data('.dygraph_columns','ts,rilevazioni_TF_IN_valore')

        fb = bc.contentPane(region='top').formbuilder()
        fb.dbSelect(value='^.componente_id',lbl='Componente',
                    dbtable='mchn.componente')
        fb.numberTextBox(value='^.limit',lbl='Limite rilevazioni',
                    width='5em')
        tc =  bc.tabContainer(region='center',margin='2px')
        tc.contentPane(title='Opzioni grafico').multiValueEditor(value='^.dygraph_options')

        


