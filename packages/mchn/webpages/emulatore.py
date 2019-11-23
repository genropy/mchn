# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'public:Public,th/th:TableHandler'
    def main(self,root,**kwargs):
        bc = root.rootBorderContainer(title='Emulatore misurazione componenti',datapath='main')
        self.parametri(bc.roundedGroup(title='Parametri',region='top',height='150px'))
        bc.contentPane(region='center'
                        ).plainTableHandler(table='mchn.componente_rilevazione',
                                            viewResource='ViewFromEmulatore',count=True,
                                            pbl_classes=True,view_store_limit=100)
    def parametri(self,pane):
        fb = pane.formbuilder(cols=3)
        fb.checkbox(value='^.active',label='!![it]Attiva rilevazioni')
        fb.numberTextbox(value='^.timing',lbl='Timing')
        pane.data('.timing',30)
        pane.dataRpc(None,self.db.table('mchn.componente').popola_rilevazioni_componenti,
                    _timing='^.timing',
                    _active='^.active',_if='_active')