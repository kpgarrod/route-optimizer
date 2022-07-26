# -*- coding: utf-8 -*-
# from odoo import http


# class Route-optimiser(http.Controller):
#     @http.route('/route-optimiser/route-optimiser/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/route-optimiser/route-optimiser/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('route-optimiser.listing', {
#             'root': '/route-optimiser/route-optimiser',
#             'objects': http.request.env['route-optimiser.route-optimiser'].search([]),
#         })

#     @http.route('/route-optimiser/route-optimiser/objects/<model("route-optimiser.route-optimiser"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('route-optimiser.object', {
#             'object': obj
#         })
