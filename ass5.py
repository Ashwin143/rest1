# import thread

# class PrtArg(object):
#     @staticmethod
#     def name1(tname,*args):
#         cnt = 0
#         print("Inside print_name1")
#         while cnt < 10:
#             cnt += 1
#             print("%s : %s\n" % (tname, cnt))

#     @staticmethod
#     def name(tname,*args):
#         cnt = 0
#         print("Inside print_name")
#         while cnt < 10:
#             cnt += 1
#             print ("%s : %s\n" % (tname, cnt))

#     def m_prt(self,*args):
#         thread.start_new_thread(PrtArg.name, (args[0],))
#         thread.start_new_thread(PrtArg.name1, (args[1],))
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# date_after_month = datetime.today()+ relativedelta(months=3)

# print ('Today: ',datetime.today().strftime('%d/%m/%Y'))
# print( 'After Month:', date_after_month.strftime('%d/%m/%Y'))
