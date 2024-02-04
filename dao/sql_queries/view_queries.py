def get_searches():
    query = """select s.id, s.user_id, 
        (select ci.name from cities ci where s.city_from_id=ci.id) as city_from, 
        (select ci.name from cities ci where s.city_to_id=ci.id) as city_to,
        s.date_min,
        s.date_max,
        s.days_min,
        s.days_max
        from searches s"""
    return query

def get_search_by_id(id):
    return f"{get_searches()} WHERE s.id={id}"