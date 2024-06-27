# -*- coding: utf-8 -*-

from odoo import models, fields, api



class BatimentGestion(models.Model):
    _name = 'batiment.gest'
    _description = 'Gestion des Bâtiments'

    name = fields.Char(string='Nom du Bâtiment', required=True)
    address = fields.Char(string='Adresse')
    city = fields.Char(string='Ville')
    state = fields.Char(string='État')
    zip_code = fields.Char(string='Code Postal')
    country_id = fields.Many2one('res.country', string='Pays')
    description = fields.Text(string='Description')

    



class ChambreGestion(models.Model):
    _name = 'chambre.gest'
    _description = 'Gestion Hotel'

    piece_nombre = fields.Char(string='Nombre de pièces')
    styleChambre = fields.Char(string='Style de la chambre')
    statut = fields.Char(required=True, string='Statut')
    description = fields.Text(string='Description')





class CommoditesGestion(models.Model):
    _name = 'commodites.gest'
    _description = 'Gestion des Commodités'

    name = fields.Char(string='Nom de la Commodité', required=True)
    room_service = fields.Char(string='Service de Chambre')
    wifi = fields.Boolean(string='Wi-Fi')
    tv = fields.Boolean(string='TV')
    minibar = fields.Boolean(string='Minibar')
    air_conditioning = fields.Boolean(string='Climatisation')
    description = fields.Text(string='Description')





class ClientGestion(models.Model):
    _name = 'client.gest'
    _description = 'Gestion des Clients'

    nom = fields.Char(string='Nom')
    prenom = fields.Char(string='Prénom')
    id_numero = fields.Char(string='Numéro d\'ID')
    description = fields.Text(string='Description')




class ReservationGestion(models.Model):
    _name = 'reservation.gest'
    _description = 'Gestion des Réservations'

    type_chambre = fields.Char(string='Type de Chambre')
    espace = fields.Char(string='Espace')
    date_reservation_entrer = fields.Char(string='Date d\'Entrée')
    date_reservation_sortie = fields.Char(string='Date de Sortie')
    description = fields.Text(string='Description')


class PayementGestion(models.Model):
    _name = 'payement.gest'
    _description = 'Gestion des Paiements'

    type_de_payement = fields.Char(string='Type de Paiement')
    statut_de_payement = fields.Char(string='Statut de Paiement')

class EspaceGestion(models.Model):
    _name = 'espace.gest'
    _description = 'Gestion des Espaces'

    type_espace = fields.Integer(string='Type d\'Espace')
    statut_espace = fields.Integer(string='Statut de l\'Espace')
    description = fields.Text(string='Description')



class Staff(models.Model):
    _name = 'staff'
    _description = 'Staff Information'

    name = fields.Char(string='Nom', required=True)
    role = fields.Char(string='Rôle')
    department = fields.Many2one('department', string='Département')
    phone = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')
    image = fields.Binary(string='Image')
    active = fields.Boolean(string='Actif', default=True)
    dateEmbauche = fields.Date(string='Date d\'Embauche', default=fields.Date.context_today)



