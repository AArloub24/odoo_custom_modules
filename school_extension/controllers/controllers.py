# -*- coding: utf-8 -*-
from odoo import http

# class SchoolExtension(http.Controller):
#     @http.route('/school_extension/school_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_extension/school_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_extension.listing', {
#             'root': '/school_extension/school_extension',
#             'objects': http.request.env['school_extension.school_extension'].search([]),
#         })

#     @http.route('/school_extension/school_extension/objects/<model("school_extension.school_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_extension.object', {
#             'object': obj
#         })