# -*- coding: utf-8 -*-
from qgis.core import *
from qgis.utils import qgsfunction
from datetime import datetime
import json


@qgsfunction(args='auto', group='Geocity')
def get_permit_amend_properties(feature, parent):
    """
    Function to get a string output from a list of actors
    """
    get_keys = True
    field_names = [field.name() for field in feature.fields()]
    d = dict(zip(field_names, feature.attributes()))
    amend_properties = json.loads(d['amend_properties'])
    retval = ''
    retval += "<style>body{font-family: arial; font-size: 12px;}</style>"
    print(f"amend_properties: {amend_properties}")
    lr = '<br>'
    for i, amend_property in amend_properties.items():
        strline = f"<h3>{i}</h3>"
        retval += strline
        for k, v in amend_property.items():
            if get_keys:
                strline = f"<dl><dt>{lr}property_{k}:</dt> <dd>{v}{lr}</dd></dl>" if str(k) == 'id' else f"<dl><dt>{k}:</dt> <dd>{v}{lr}</dd></dl>"
            else:
                strline = f"<dl><dt>property_{v}{lr}</dt></dl>" if str(k) == 'id' else f"<dl><dt>{v}{lr}</dt></dl>"
            retval += strline

    return(retval)


@qgsfunction(args='auto', group='Geocity')
def get_permit_author(feature, parent):
    """
    Function to get a string output from a list of actors
    """
    get_keys = False
    field_names = [field.name() for field in feature.fields()]
    d = dict(zip(field_names, feature.attributes()))
    author = json.loads(d['author'])
    retval = ''
    retval += "<style>body{font-family: arial; font-size: 12px;}th, td{padding: 0px;  text-align: left; font-size: 12px;}</style>"
    lr = '<br>'
    ts = '&#8239;'
    for i, (k, author) in enumerate(author.items()):
        retval += "<table>"
        if get_keys:
            strline = f"{lr}author_{k}: {author}{lr}" if str(k) == 'id' else f"{k}: {author}{lr}"
        else:
            keys = [
                f"Prénom{ts}:",
                f"Nom{ts}:",
                f"Adresse{ts}:",
                f"NPA{ts}:",
                f"Localité{ts}:",
                f"Raison sociale{ts}:",
                f"Numéro TVA{ts}:",
                f"Téléphone{ts}:",
                f"Téléphone (2){ts}:",
                f"E-mail{ts}:"
            ]
            #strline = f"{author}{lr}" if str(i) == 'id' else f"{author}{lr}"
            strline = f"<tr><th>{keys[i]}</th> <td>{author}</td></tr>"
        retval += strline
        retval += "</table>"

    return(retval)


@qgsfunction(args='auto', group='Geocity')
def get_permit_contacts(pos, feature, parent):
    """
    Function to get a string output from a list of actors
    """
    try:
        pos
    except NameError:
        pos = 0

    get_keys = False
    field_names = [field.name() for field in feature.fields()]
    d = dict(zip(field_names, feature.attributes()))
    permit_request_actors = json.loads(d['permit_request_actor'])
    retval = ''
    retval += "<style>body{font-family: arial; font-size: 12px;}th, td{padding: 0px;  text-align: left; font-size: 12px;}</style>"
    print(f"permit_request_actors: {permit_request_actors}")
    lr = '<br>'
    ts = '&#8239;'
    for i, (j, actor) in enumerate(permit_request_actors.items()):
        if (pos==i):
            strline = f"<h3>{j}</h3>"
            retval += strline
            retval += "<table>"
            for idx, (k, v) in enumerate(actor.items()):
                if get_keys:
                    strline = f"{lr}contact_{k}: {v}{lr}" if str(k) == 'id' else f"{k}: {v}{lr}"
                else:
                    keys = [
                        f"Type{ts}:",
                        f"Identifiant{ts}:",
                        f"Prénom{ts}:",
                        f"Nom{ts}:",
                        f"Raison sociale{ts}:",
                        f"Numéro TVA{ts}:",
                        f"Adresse{ts}:",
                        f"NPA{ts}:",
                        f"Localité{ts}:",
                        f"Téléphone{ts}:",
                        f"E-mail{ts}:"
                    ]
                    strline = f"<tr><th>{keys[idx]}</th> <td>contact_{v}</td></tr>" if str(k) == 'id' else f"<tr><th>{keys[idx]}</th> <td>{v}</td></tr>"
                retval += strline
            retval += "</table>"

    return(retval)


@qgsfunction(args='auto', group='Geocity')
def get_permit_request_properties(feature, parent):
    """
    Function to get a string output from a list of actors
    """
    get_keys = True
    field_names = [field.name() for field in feature.fields()]
    d = dict(zip(field_names, feature.attributes()))
    request_properties = json.loads(d['request_properties'])
    retval = ''
    retval += "<style>body{font-family: arial; font-size: 12px;}th, td{padding: 0px;  text-align: left; font-size: 12px;}</style>"
    print(f"request_properties: {request_properties}")
    lr = '<br>'
    ts = '&#8239;'
    for i, request_property in request_properties.items():
        strline = f"<h3>{i}</h3>"
        retval += strline
        retval += "<table>"
        for idx, (k, v) in enumerate(request_property.items()):
            if get_keys:
                strline = f"<tr><th>{k}</th> <td>property_{v}</td></th>" if str(k) == 'id' else f"<tr><th>{k}</th> <td>{v}</td></tr>"
            else:
                keys = [
                        f"Largeur [m]{ts}:",
                        f"Longueur [m]{ts}:",
                        f"Marquage routier endommmagé{ts}:",
                        f"Moins de 3m d'un tronc d'arbre ou haie{ts}:",
                        f"Sur la chaussée{ts}:",
                        f"Sur une surface verte{ts}:",
                        f"Sur un trottoir{ts}:",
                        f"Description{ts}:",
                        f"Documents complémentaires{ts}:"
                    ]
                strline = f"<tr><th>{v}</th></tr>" if str(k) == 'id' else f"<tr><th>{v}</th></tr>"
                strline = f"<tr><th>{keys[idx]}</th> <td>property_{v}</td></th>" if str(k) == 'id' else f"<tr><th>{keys[idx]}</th> <td>{v}</td></tr>"
            retval += strline
        retval += "</table>"

    return(retval)


@qgsfunction(args='auto', group='Geocity')
def get_permit_validations(feature, parent):
    """
    Function to get a string output from a list of actors
    """
    get_keys = False
    field_names = [field.name() for field in feature.fields()]
    d = dict(zip(field_names, feature.attributes()))
    validations = json.loads(d['validations'])
    retval = ''
    retval += "<style>body{font-family: arial; font-size: 12px;}</style>"
    lr = '<br>'
    ts = '&#8239;'
    for i, (j, validation) in enumerate(validations.items()):
        strline = f"<h3>{j}</h3>"
        retval += strline
        for idx, (k, v) in enumerate(validation.items()):
            if get_keys:
                strline = f"<dl><dt>{lr}validation_{k}:</dt> <dd>{v}{lr}</dd></dl>" if str(k) == 'id' else f"<dl><dt>{k}:</dt> <dd>{v}{lr}</dd></dl>"
            else:
                keys = [
                    f"Statut{ts}:",
                    f"Commentaire (avant){ts}:",
                    f"Commentaire (pendant){ts}:",
                    f"Commentaire (après){ts}:"
                ]
                strline = f"<dl><dt>{keys[idx]}</dt><dd>validation_{v}{lr}</dd></dl>" if str(k) == 'id' else f"<dl><dt>{keys[idx]}</dt><dd>{v}{lr}</dd></dl>"
            retval += strline

    return(retval)


class GeocityExpressions:
    def __init__(self, serverIface):
        QgsMessageLog.logMessage(
            "******Loading expressions********", "GeocityExpressions", Qgis.Info
        )
        QgsExpression.registerFunction(get_permit_amend_properties)
        QgsExpression.registerFunction(get_permit_author)
        QgsExpression.registerFunction(get_permit_contacts)
        QgsExpression.registerFunction(get_permit_request_properties)
        QgsExpression.registerFunction(get_permit_validations)
