import mysql.connector as x
z=x.connect(host='localhost',user='root',password='dpsd')
cur=z.cursor()
q=cur.execute('drop database if exists project;')
q=cur.execute('create database project;')
q=cur.execute('use project;')
q=cur.execute('create table project(name char(20),code int primary key,quantity int,price int);')
q=cur.execute('insert into project values("biscuits",111,50,10);')
q=cur.execute('insert into project values("chips",222,50,10);')
q=cur.execute('insert into project values("bread",333,15,25);')
q=cur.execute('insert into project values("flour",444,65,80);')
q=cur.execute('insert into project values("pulses",555,45,30);')
q=cur.execute('insert into project values("rice",666,21,78);')
print('\t\t\t\tGSSMS')
print('\t\t\t\t','-'*4,sep='-')
print('\t\tGROCERY STORE STOCK MANAGEMENT SYSTEM')
print('\t\t','-'*36,sep='-')
print('\n')
while True:
    b=int(input('\tI am :- \n\t 1.customer \n\t 2.Grocer \n\t 3.exit \n\n\t\t ENTER CHOICE \t'))
    if b==1:
        while True:
              print('\n')
              print('*-'*39,'\n')
              print('\tMENU:')
              print('\t1.Show Stock')
              print('\t2.Search Stock')
              print('\t3.Exit')
              ai=(int(input('\n\t\tENTER CHOICE   ')))
              if ai==1:
                   print('\n\tSUBMENU:')
                   print('\tShow Stock By:-')
                   print('\t1.Name')
                   print('\t2.Code')
                   print('\t3.Quantity')
                   print('\t4.Price')
                   bi=(int(input('\n\t\tENTER CHOICE   ')))
                   if bi==1:
                       q=cur.execute('select name from project;')
                       f=cur.fetchall()
                       print('\n')
                       for i in range (len(f)):
                           print('\t\t',f[i][0])
                   elif bi==2:
                       q=cur.execute('select code from project;')
                       f=cur.fetchall()
                       print('\n')
                       for i in range(len(f)):
                           print('\t\t',f[i][0])
                   elif bi==3:
                       q=cur.execute('select quantity from project;')
                       f=cur.fetchall()
                       print('\n')
                       for i in range(len(f)):
                           print('\t\t',f[i][0])
                   elif bi==4:
                       q=cur.execute('select price from project;')
                       f=cur.fetchall()
                       print('\n')
                       for i in range(len(f)):
                           print('\t\t',f[i][0])
                   else:
                       print('\n\tsorry :-( \n\tincorect choice, please type again \n')
              elif ai==2:
                   print('\n\tSUBMENU:')
                   print('\tSearch Stock By:-')
                   print('\t1.Name')
                   print('\t2.Code')
                   print('\t3.Quantity')
                   print('\t4.Price')
                   ci=(int(input('\n\t\tENTER CHOICE   ')))
                   if ci==1:
                        a1=input('\t\tenter item name   ')
                        q=cur.execute('select name from project;')
                        f=cur.fetchall()
                        if (str(a1.lower()),) in f:
                            print('\n\t\tyay!!! item available')
                        else:
                            print('\n\t\tsorry :-( \n\t\titem not available, please try something else')
                   elif ci==2:
                        a2=int(input('\n\tenter item code   '))
                        q=cur.execute('select code from project;')
                        f=cur.fetchall()
                        if (a2,) in f:
                            print('\n\t\tyay!!! item available')
                        else:
                            print('\n\t\tsorry :-( \n\t\titem not available, please try something else')
                   elif ci==3:
                        a3=int(input('\n\tenter item quantity   '))
                        q=cur.execute('select quantity from project;')
                        f=cur.fetchall()
                        if (a3,) in f:
                            print('\n\t\tyay!!! item available')
                        else:
                            print('\n\t\tsorry :-( \n\t\titem not available, please try something else')
                   elif ci==4:
                        a4=int(input('\n\tenter item price   '))
                        q=cur.execute('\n\tselect price from project;')
                        f=cur.fetchall()
                        if (a4,) in f:
                            print('\n\t\tyay!!! item available')
                        else:
                            print('\n\t\tsorry :-( \n\t\titem not available, please try something else')
                   else:
                       print('\n\tsorry :-( \n\tincorect choice, please type again \n')
              elif ai==3:
                   print('*-'*39,'\n')
                   break
              else:
                  print('\n\t\tsorry :-( \n\t\tincorect choice, please type again')
    elif b==2:
         a=int(input('\n\t\tenter password       '))
         if a==2024:
              while True:
                   print('\n')
                   print('*-'*39)
                   print('\n\tMENU:')
                   print('\t1.Show Stock')
                   print('\t2.Add Stock')
                   print('\t3.Update Stock')
                   print('\t4.Search Stock')
                   print('\t5.Delete Stock')
                   print('\t6.Generate Bill')
                   print('\t7.Exit')
                   ah=(int(input('\n\t\tENTER CHOICE   ')))
                   if ah==1:
                             print('\n\tSUBMENU:')
                             print('\tShow Stock By:-')
                             print('\t1.Name')
                             print('\t2.Code')
                             print('\t3.Quantity')
                             print('\t4.Price')
                             bh=(int(input('\n\t\tENTER CHOICE   ')))
                             if bh==1:
                                 q=cur.execute('select name from project;')
                                 f=cur.fetchall()
                                 print('\n')
                                 for i in range (len(f)):
                                     print('\t\t',f[i][0])
                             elif bh==2:
                                 q=cur.execute('select code from project;')
                                 f=cur.fetchall()
                                 print('\n')
                                 for i in range(len(f)):
                                     print('\t\t',f[i][0])
                             elif bh==3:
                                 q=cur.execute('select quantity from project;')
                                 f=cur.fetchall()
                                 print('\n')
                                 for i in range(len(f)):
                                     print('\t\t',f[i][0])
                             elif bh==4:
                                 q=cur.execute('select price from project;')
                                 f=cur.fetchall()
                                 print('\n')
                                 for i in range(len(f)):
                                     print('\t\t',f[i][0])
                             else:
                                 print('\n\tsorry :-( \n\tincorect choice, please type again \n')
                   elif ah==2:
                             b1=input('\t\tenter item name   ')
                             b2=int(input('\t\tenter code   '))
                             b3=int(input('\t\tenter quantity   '))                             
                             b4=int(input('\t\tenter price   '))
                             q=cur.execute('insert into project values("{}",{},{},{});'.format(b1,b2,b3,b4))
                             print('\n\t\t\tyay!!! item added successfully')
                   elif ah==3:
                             print('\n\tSUBMENU:')
                             print('\tUpdate Stock By:-')
                             print('\t1.Name')
                             print('\t2.Code')
                             print('\t3.Quantity')
                             print('\t4.Price')
                             dh=(int(input('\n\t\tENTER CHOICE   ')))
                             if dh==1:
                                 t1=input('\t\tenter item name to be updated   ')
                                 q=cur.execute('select name from project;')
                                 f=cur.fetchall()
                                 if (str(t1.lower()),) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     t2=input('\t\tenter new name   ')
                                     q=cur.execute('update project set name="{}" where name="{}"'.format(t2,t1))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\tname updated')
                             elif dh==2:
                                 t1=int(input('\t\tenter item code to be updated   '))
                                 q=cur.execute('select code from project;')
                                 f=cur.fetchall()
                                 if (t1,) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     t2=input('\t\tenter new code   ')
                                     q=cur.execute('update project set code={} where code={};'.format(t2,t1))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\tcode updated')
                             elif dh==3:
                                 t1=int(input('\t\tenter item quantity to be updated   '))
                                 q=cur.execute('select quantity from project;')
                                 f=cur.fetchall()
                                 if (t1,) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     t2=input('\t\tenter new quantity   ')
                                     q=cur.execute('update project set quantity={} where quantity={}'.format(t2,t1))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\tquantity updated')
                             elif dh==4:
                                 t1=int(input('\t\tenter item price to be updated   '))
                                 q=cur.execute('select price from project;')
                                 f=cur.fetchall()
                                 if (t1,) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     t2=input('\t\tenter new price   ')
                                     q=cur.execute('update project set price={} where price={}'.format(t2,t1))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\tprice updated')
                             else:
                                 print('\n\tsorry :-( \n\tincorect choice, please type again \n')
                   elif ah==4:
                             print('\n\tSUBMENU:')
                             print('\tSearch Stock By:-')
                             print('\t1.Name')
                             print('\t2.Code')
                             print('\t3.Quantity')
                             print('\t4.Price')
                             eh=(int(input('\n\t\tENTER CHOICE   ')))
                             if eh==1:
                                 a1=input('\t\tenter item name   ')
                                 q=cur.execute('select name from project;')
                                 f=cur.fetchall()
                                 if (str(a1.lower()),) in f:
                                     print('\n\t\t\tyay!!! item available')
                                 else:
                                     print('\n\t\t\tsorry :-( \n\t\t\titem not available, please try something else')
                             elif eh==2:
                                 a2=int(input('\t\tenter item code   '))
                                 q=cur.execute('select code from project;')
                                 f=cur.fetchall()
                                 if (a2,) in f:
                                     print('\n\t\t\tyay!!! item available')
                                 else:
                                     print('\n\t\t\tsorry :-( \n\t\t\titem not available, please try something else')
                             elif eh==3:
                                 a3=int(input('\t\tenter item quantity   '))
                                 q=cur.execute('select quantity from project;')
                                 f=cur.fetchall()
                                 if (a3,) in f:
                                     print('\n\t\t\tyay!!! item available')
                                 else:
                                     print('\n\t\t\tsorry :-( \n\t\t\titem not available, please try something else')
                             elif eh==4:
                                 a4=int(input('\t\tenter item price   '))
                                 q=cur.execute('select price from project;')
                                 f=cur.fetchall()
                                 if (a4,) in f:
                                     print('\n\t\t\tyay!!! item available')
                                 else:
                                     print('\n\t\t\tsorry :-( \n\t\t\titem not available, please try something else')
                             else:
                                 print('\n\tsorry :-( \n\tincorect choice, please type again \n')
                   elif ah==5:
                             print('\n\tSUBMENU:')
                             print('\tDelete Stock By:-')
                             print('\t1.Name')
                             print('\t2.Code')
                             print('\t3.Quantity')
                             print('\t4.Price')
                             fh=(int(input('\n\t\tENTER CHOICE   ')))
                             if fh==1:
                                 t1=input('\t\tenter item name to be deleted   ')
                                 q=cur.execute('select name from project;')
                                 f=cur.fetchall()
                                 if (str(t1.lower()),) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     q=cur.execute('delete from project where name="%s"'%(t1,))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\titem deleted')
                             elif fh==2:
                                 t1=int(input('\t\tenter item code to be deleted   '))
                                 q=cur.execute('select code from project;')
                                 f=cur.fetchall()
                                 if (t1,) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     q=cur.execute('delete from project where code=%s'%(t1,))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\titem deleted')
                             elif fh==3:
                                 t1=int(input('\t\tenter item quantity to be deleted   '))
                                 q=cur.execute('select quantity from project;')
                                 f=cur.fetchall()
                                 if (t1,) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     q=cur.execute('delete from project where quantity=%s'%(t1,))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\titem deleted')
                             elif fh==4:
                                 t1=int(input('\t\tenter item price to be deleted   '))
                                 q=cur.execute('select price from project;')
                                 f=cur.fetchall()
                                 if (t1,) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     q=cur.execute('delete from project where price=%s'%(t1,))
                                     print('\n\t\t\tsuccess ;-D \n\t\t\titem deleted')
                             else:
                                 print('\n\tsorry :-( \n\tincorect choice, please type again \n')
                   elif ah==6:
                             ai1=int(input('\n\t enter no. of items purchased      '))
                             aii=ai1
                             q=cur.execute('drop table if exists pro;')
                             q=cur.execute('create table pro(name char(20),quantity int,price int,total_price int);')
                             while ai1>0:
                                 ai2=(input('\n\t\t item name    '))
                                 q=cur.execute('select name from project;')
                                 f=cur.fetchall()
                                 if (str(ai2.lower()),) not in f:
                                     print('\n\t\t\toops!!! error, item is not available')
                                 else:
                                     ai3=int(input('\t\t enter quantity      '))
                                     q=cur.execute('select price from project where name = "{}"'.format(ai2.lower()))
                                     f=cur.fetchall()
                                     ai4=ai3*f[0][0]
                                     q=cur.execute('insert into pro values("{}",{},{},{});'.format(ai2.lower(),ai3,f[0][0],ai4))
                                     ai1-=1
                             print('\n')
                             print('\t                  BILL\n')
                             print('\t  Name   ','Quantity   ','Price   ','Total Price')
                             q=cur.execute('select * from pro;')
                             r=cur.fetchall()
                             for j in range (aii):
                                 print('\t',r[j][0],'   ',r[j][1],'       ',r[j][2],'       ',r[j][3])
                             q=cur.execute('select sum(total_price)"grand total" from pro;')
                             r=cur.fetchall()
                             print('\tGrand Total-                  ',r[0][0],'rs.')
                             print('\n\tThanks for coming :-) \n\tsee you soon!!!')
                   elif ah==7:
                        print('*-'*39,'\n')
                        break
                   else:
                       print('\n\tsorry :-( \n\tincorect choice, please type again')                       
         else:
             print('\n\toh no :-( \n\tpassword is incorrect, please type again')
             print('\t')
    elif b==3:
        print('\n\tTHANKS FOR USING   :-)')
        print('*-'*39,'\n')
        break
    else:
        print('\n\tsorry :-( \n\tincorect choice, please type again \n')
        print('*-'*39,'\n')
z.commit()
cur.close()
z.close()