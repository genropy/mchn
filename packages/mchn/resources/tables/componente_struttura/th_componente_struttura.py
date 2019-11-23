#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    def th_hiddencolumns(self):
        return '$_h_count'

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('hierarchical_descrizione',width='30em')
        r.fieldcell('geocoder',width='10em')

    def th_order(self):
        return '_h_count'

    def th_query(self):
        return dict(column='hierarchical_descrizione', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('descrizione')
        fb.field('geocoder')
        tc = bc.tabContainer(region='center',margin='2px')
        th = tc.contentPane(title='Componenti').dialogTableHandler(relation='@componenti',formResource='FormFromStruttura')
        form.htree.relatedTableHandler(th,dropOnRoot=False,inherited=True)
        self.strutturaMappa(tc.borderContainer(title='Mappa',
                                                datapath='#FORM.map_localizer',
                                                parentForm=False))
        
    
    def strutturaMappa(self,bc):
        """
        Giovanni Porcari, [22 nov 2019, 11:56:17]:
<script src="https://assets.what3words.com/sdk/v3/what3words.js?key=YOUR_API_KEY"></script>

what3words.api.convertTo3wa({lat:51.508344, lng:-0.12549900}).then(function(response) {
   console.log("[convertTo3wa]", response);
});
        
what3words.api.convertToCoordinates("filled.count.soap").then(function(response) {
   console.log("[convertToCoordinates]", response);
});
        """
        fb = bc.contentPane(region='top').formbuilder(cols=4, border_spacing='4px')
        fb.geoCoderField(value='^.fulladdress',lbl='Full Address',country='IT',
                       selected_position='.map_center',
                       width='30em')
        fb.textbox(value='^.what3words',lbl='W3W')
        fb.textbox(value='^.map_center',lbl='Map center')
        #fb.textbox(value='^.map_type',lbl='Map type',default='roadmap')
        #fb.numberTextbox(value='^.map_zoom',lbl='Map zoom')
        center = bc.contentPane(region='center')
        
        m = center.GoogleMap(height='100%', width='100%',
                        #position='absolute',top=0,left=0,right=0,bottom=0,
                     #map_type='^.map_type',
                     selfsubscribe_clickLatLng="""
                     SET #FORM.record.geocoder = $1.lat+','+$1.lng;""",
                     map_event_rightclick="""
                                            console.log(kw);
                                            this.publish("clickLatLng",{
                                                            lat:kw.latLng.lat(),
                                                            lng:kw.latLng.lng()
                                                            });""",
                     map_center='^.map_center',
                     nodeId='gma',
                     #centerMarker=dict(title='Sede Incarico', label='X'),
                     autoFit=True,
                     map_zoom=16,
                    # map_disableDefaultUI=True,
                     )
        center.dataController(geocoder='^#FORM.record.geocoder')

        center.dataController(""" 
            if(!m.map){
                return;
            }
            if(!geocoder){
                return;
            }
            m.gnr.setMarker(m,pkey,geocoder,{title:title,
                                labelContent:title[0],
                                labelAnchor: new google.maps.Point(15, 0),
                                labelClass: "markerlabel", // the CSS class for the label
                                });
            """,
            m=m,geocoder='^#FORM.record.geocoder',
            title='=#FORM.record.descrizione?=(#v || "Componente")',
            pkey='=#FORM.pkey',_delay=100)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px',hierarchical=True)
