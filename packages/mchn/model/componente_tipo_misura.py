
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_tipo_misura', pkey='id', name_long='!!Misura Tipo Componente', name_plural='!!Misure Tipo Componente',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('componente_tipo_id', size='22').relation('componente_tipo.id', 
                                                mode='foreignkey', 
                                                relation_name='valori_misurabili')
        tbl.column('descrizione', name_long='!!Descrizione')
        tbl.column('misura_tipo_id', size='22', name_long='!!Tipo misura').relation('misura_tipo.id', mode='foreignkey')
        tbl.column('valore_minimo_override', dtype='dec', name_long='!!Valore minimo')
        tbl.column('valore_minimo_override', dtype='dec', name_long='!!Valore massimo')
        tbl.formulaColumn('valore_minimo', 'COALESCE($valore_minimo_override,@misura_tipo_id.valore_minimo)', name_long='Valore Minimo')
        tbl.formulaColumn('valore_massimo', 'COALESCE($valore_minimo_override,@misura_tipo_id.valore_massimo)', name_long='Valore Massimo')
        tbl.aliasColumn('step', '@misura_tipo_id.step')
        tbl.aliasColumn('tipo_dato', '@misura_tipo_id.tipo_dato')
        tbl.column('impostabile', dtype='B', name_long="Impostabile")