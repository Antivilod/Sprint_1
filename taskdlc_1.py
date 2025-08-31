def remove_duplicates(tickets_dict):
    used_tickets = set()
    result = {}
    
    for level in sorted(tickets_dict.keys()):
        unique_for_level = []
        for ticket in tickets_dict[level]:
            if ticket not in used_tickets:
                unique_for_level.append(ticket)
                used_tickets.add(ticket)
        
        result[level] = unique_for_level
    
    return result

def group_tickets(types_dict, tickets_dict):
    unique_tickets = remove_duplicates(tickets_dict)
   
    result = {}
    
    for level, tickets_list in unique_tickets.items():
        criticality_level = types_dict[level]
        result[criticality_level] = tickets_list

    return result
    
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
