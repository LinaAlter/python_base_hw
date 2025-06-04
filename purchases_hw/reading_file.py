import json
dict_purchases = {}
with open('purchase_log.txt', 'r', encoding='UTF-8') as f_pur:
    for line in f_pur:
        line = line.strip()
        purchases = json.loads(line)
        user_id = purchases.get('user_id')
        category =  purchases.get('category')
        if user_id and category:
            dict_purchases[user_id] = category 
 
    
with open('visit_log.csv', 'r', encoding='UTF-8') as f_vis:
    with open('funnel.csv', 'w', encoding='UTF-8') as f_fun:
        for visit in f_vis:
            user_id = visit.strip().split(',')[0]
            if user_id in dict_purchases:
                new_line = f'{visit.strip()},{dict_purchases[user_id]}\n'
                f_fun.write(new_line)
           
            
            
        
       



    

