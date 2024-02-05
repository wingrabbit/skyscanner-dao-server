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

def get_top_prices_by_search_id(search_id, limit=15):
    query = f"""WITH sub_q AS 
            (SELECT
            r.date_from,
            r.date_return, 
            (SELECT ci.name FROM cities ci WHERE s.city_from_id=ci.id) AS city_from, 
            (SELECT ci.name FROM cities ci WHERE s.city_to_id=ci.id) AS city_to,
            pr.price,
            pr.stops
            FROM prices pr
            INNER JOIN results r ON pr.result_id=r.id
            INNER JOIN searches s ON r.search_id=s.id
            WHERE s.id={search_id}
            ORDER BY stops, price ASC)
        (SELECT * FROM sub_q WHERE stops=0 LIMIT {limit})
        UNION ALL (SELECT * FROM sub_q WHERE stops=1 LIMIT {limit})
        UNION ALL (SELECT * FROM sub_q WHERE stops=2 LIMIT {limit})"""
    return query