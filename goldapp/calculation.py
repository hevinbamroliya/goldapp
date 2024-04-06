# import frappe

# @frappe.whitelist()
# def custom_total_amount(net_weight, fine_weight, gross_weight, less_weight):
#     c_net_weight = 0
#     c_fine_weight = 0
#     c_gross_weight = 0
#     c_less_weight = 0
#     total_amount = [net_weight, fine_weight, gross_weight, less_weight]
#     for i in total_amount:
#         c_net_weight = net_weight + i
#         c_fine_weight = fine_weight + i 
#         c_gross_weight = gross_weight + i
#         c_less_weight = less_weight + i
    
#     return(c_net_weight, c_fine_weight, c_gross_weight, c_less_weight)


