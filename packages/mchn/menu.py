#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    impianti = root.branch(u"Impianti")
    impianti.thpage("Componente", table="mchn.componente")
    impianti.thpage("Rilevazione", table="mchn.componente_rilevazione")
    impianti.thpage("Struttura", table="mchn.componente_struttura")
    impianti.thpage("Tipi componente", table="mchn.componente_tipo")
    impianti.thpage("Tipi misurazione", table="mchn.componente_tipo_misura")
    impianti.thpage("Misura tipo", table="mchn.misura_tipo")
    impianti.lookups("Tabelle Ausiliarie", lookup_manager="mchn")


