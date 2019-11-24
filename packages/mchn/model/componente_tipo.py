# encoding: utf-8
from gnr.core.gnrdecorator import public_method

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_tipo', pkey='id', 
                        name_long='!!Tipo Componente', 
                        name_plural='!!Tipi Componenti',
                        caption_field='descrizione')
        self.sysFields(tbl,hierarchical='descrizione,codice',hierarchical_root_id=True,df=True)
        tbl.column('codice',size=':10', name_long='!!Codice')
        tbl.column('descrizione', name_long='!!Descrizione')



    @public_method
    def getStrutturaRipartizioni(self,tipo_id=None,componente_id=None,colonnaComponente=False):
        if componente_id:
            componente = self.db.table('mchn.componente').record(componente_id).output('dict')
            tipo_id = componente['componente_tipo_id']
        struct = self.db.currentPage.newGridStruct('mchn.componente_rilevazione')
        r = struct.view().rows()
        r.fieldcell('ts',width='12em',name='Data e ora')
        if colonnaComponente:
            r.fieldcell('@componente_id.descrizione',width='10em')
        if tipo_id:
            tipi_misura = self.db.table('mchn.componente_tipo_misura'
                        ).query(where='$componente_tipo_id=:tipo_id',
                                columns='*,$tipo_dato,$step,$valore_minimo,$valore_massimo',
                                tipo_id=tipo_id).fetch()
            for tm in tipi_misura:
                r.cell('rilevazioni_{}_valore'.format(tm['misura_codice']),
                            width='7em',dtype=tm['tipo_dato'],
                            name=tm['misura_codice'].replace('_',' '))
        return struct