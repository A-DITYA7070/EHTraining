HQL :- Hibernate query language is an object oriented query language, similar to sql but instead of operating on tables and columns, hql works with persistent objects and their properties.
       HQL queries are translated by Hibernate into conventional sql queries, which in turns perform action on db.

+> we can use sql statements directly with hibernate using native sql, but hql is recommended to avoid database portability hassles, and to take advantage of hibernate sql generation and 
caching strategies.

EX :- String hql = "FROM Employee";
      Query query = session.createQuery(hql);
      List results = query.list();

      or 

      String hql = "From com.hibernatebook.criteria.Empoyee";
      Query query = session.createQuery(hql);
      List results = query.list();


HQL VULNERABALITIES :>> <<:


      
