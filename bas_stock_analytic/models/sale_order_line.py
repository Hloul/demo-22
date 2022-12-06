# -*- coding: utf-8 -*-
# Part of BAS. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_is_zero, float_compare
from datetime import datetime
from collections import namedtuple, OrderedDict, defaultdict

_logger = logging.getLogger(__name__)


    
class SaleOrderLine(models.Model):
    
    _inherit = 'sale.order.line'


    def _prepare_procurement_values(self,group_id):
        res = super(SaleOrderLine,self)._prepare_procurement_values(group_id=group_id)
        _logger.info('bas: self id %s',self.id)
        _logger.info('bas: analyic_distribution %s',analytic_distribution)
        res.update({
                'analytic_distribution': self.analytic_distribution,
            })
        _logger.info('bas: res %s',res)
        return res
    

