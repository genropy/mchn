# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    css_requires = 'mchn'
    py_requires = 'public:Public,th/th:TableHandler'
    def main(self,root,**kwargs):
        mainbc = root.rootBorderContainer(title='Gestione impianti',datapath='main')
        bc = mainbc.borderContainer(region='center',design='sidebar')
        self.selettoreStruttura(bc.borderContainer(region='left',width='400px',splitter=True))
        self.visoreComponenti(bc.borderContainer(region='center'))



       #fb = top.formbuilder(cols=2, border_spacing='4px')
       #fb.geoCoderField(lbl='Full Address',
       #                selected_street_address='.street_address',selected_locality='.locality',
       #                selected_postal_code='.zip',
       #                selectedRecord='.addressbag',
       #                country='IT',selected_position='.position',
       #                colspan=2,width='100%')
       #fb.textbox(value='^.street_address',lbl='Route')
       #fb.textbox(value='^.locality',lbl='Locality')
       #fb.textbox(value='^.zip',lbl='Zip')
       #fb.textbox(value='^.position',lbl='Geocoords')

    def selettoreStruttura(self,bc):


        bottom = bc.contentPane(region='bottom',height='400px')
        m = bottom.GoogleMap(height='100%', width='100%',
                        #position='absolute',top=0,left=0,right=0,bottom=0,
                     map_type='roadmap',
                     nodeId='gma',
                     #centerMarker=dict(title='Sede Incarico', label='X'),
                     autoFit=True,
                     #map_zoom=15
                    # map_disableDefaultUI=True,
                     )
        center = bc.contentPane(region='center',overflow='auto')
        center.hTableTree(table='mchn.componente_struttura',moveTreeNode=False,
                            excludeRoot=True,onChecked=True,
                            checkChildren=False,
                            getLabelClass="""
                            if(node.attr._record.geocoder){
                                return 'geocoder_structure';
                            }
                            """,
                            checked_geocoder='.geocoderPoints',
                            checked_pkey='.checkedStrutturePkeys')
    
    def visoreComponenti(self,bc):
        bc.contentPane(region='center').plainTableHandler(table='mchn.componente',
                                condition='$struttura_id IN :strutture_pkeys',
                                condition_strutture_pkeys='^main.checkedStrutturePkeys?=#v?#v.split(","):[]')
        bc.contentPane(region='bottom',height='50%'
                        ).plainTableHandler(table='mchn.componente_rilevazione', 
                            )