# <u>Chapter 4</u>: HIBERNATE





## **Topic - 1: Significance Of Hibernate**

### <u>Brief Working</u>

- **Hibernate** is used for mapping & storing data of an OOP object directly to RDBMS tables.
- The members of this object imitates the attributes of that table, that's why it is able to store them.


### <u>More Introduction</u>

- Hibernate for it features, is also known as an ORM (object relational mapping) tool.
- It's also an open-source, lightweight software under **LGPL license**.
- It uses JPA (Java persistence API) for ensuring data persistency.
- **<u>Data persistency</u>:** Ability to store backup of data in order to retain data, incase session meets a failure or interruption.
- One thing to note here is that Hibernate maps Java data types to SQL data types for storing data.



## **Topic - 2: Advantages Of Hibernate**

- Hibernate uses XML files for the mapping.
- So, one has to change configuration in XML files only to change something in its mapping behavior.
- It uses two-level cache (1st level by default) & thus performs very fast.
- HQL is the object-oriented version of SQL.
- Hibernate automatically creates tables in database, seeing the object members.
- It can also fetch data from databases, without requiring any separate application for server.



## **Topic - 3: Object Relational Mapping (ORM)**

- **<u>Metadata descriptor</u>:** Maps object codes to RDBMS in ORM tools.
- ORM gets job done with less code than the embedded SQL.



## **Topic - 4: Hibernate v/s EJB**

| Hibernate                                                                       | EJB                                                                                       |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Open-source software.                                                           | Close-source by Java E.                                                                   |
| Transparent data persistency.                                                   | No transparency in data processing.                                                       |
| Easy switching from one database to another.                                    | Difficult switching from one database to another.                                         |
| In-built module for ensuring data persistency.                                  | Dependent on EJB container for data persistency.                                          |
| Provides data persistency with its own classes, interfaces & methods.           | Uses JPA for providing data persistency.                                                  |
| Uses HQL to manage objects mapped to RDBMS.                                     | Uses JPQL to pass queries to the chosen database.                                         |
| Uses POJO (plain old Java objects) which are conventional object types in Java. | Uses EB (entity beans) which has its own naming conventions, making compatibility issues. |



## **Topic - 5: Hibernate Architecture**

### <u>Introduction</u>

- In Hibernate, there are multiple things which contribute to its attribute of data consistency.
- Uses both JPA & its own classes, interfaces and methods.

> **<u>NOTE</u>:**
> EJB uses JPA alone for data consistency, whereas Hibernate uses both JPA & its own configurations.

![Hibernate Architecture](./media/image2.png)


### <u>Configuration Class</u>

- Found in `org.hibernate.cfg` package.
- Used for activating Hibernate.
- It is also responsible for checking syntax of configuration file.
- If the syntax grammar is found correct, it creates metadata & returns that to the object.

```
Configuration cfg = new Configuration();
cfg.configure();
```


### <u>SessionFactory Interface</u>

- Found in `org.hibernate` package.
- Used for creating a session object.
- It is both immutable & thread-safe.
- **<u>Thread-safe code</u>:** A piece of code that can be accessed by multiple threads concurrently, safely.

```
SessionFactory factory = cfg.buildSessionFactory();
```


### <u>Session Interface</u>

- Found in `org.hibernate` package.
- Session object is created using `SessionFactory` object.
- It sets up connection (session) between Hibernate & database.
- However, this object is not thread-safe.
- We use this same object for performing CRUD operations.

```
Session session = factory.buildSession();
```


### <u>Transaction Interface</u>

- `Transaction` object is used when we want to perform an operation which affects the database.
- We use `commit()` method from `Transaction` to confirm making changes to database.

```
Transaction tx = session.beginTransaction();
tx.commit();
```


### <u>Query Interface</u>

- Found in `org.hibernate` package.
- A query instance is created using `Session.createQuery()`.

#### Other methods in `Query`:

```
Session.iterate();
Session.find();
setMaxResults();
setFirstResult();
```


### <u>Criteria Interface</u>

- **Criteria** is the name of API & `Criterion` is the name of class.
- It is used for retrieving data from database, in form of object instances.


### <u>XML File Example</u>

```
<?xml version = "1.0" encoding = "utf-8">

<hibernate-configuration>
	<session-factory>
		<property name="something"> Again something </property>
		<!-- MORE blah blah blah... -->
	</session-factory>
</hibernate-configuration>
```



## **Topic - 6: Hibernate Configuration**

### <u>Configuring Hibernate</u>

![Configuring Hibernate](./media/image3.png)


### <u>Creating Hibernate Session</u>

- Session acts as a bridge between the database & hibernate application.
- But many database related information is required to establish a successful connection.
- These information includes database driver name, username & password.


### <u>Creating SessionFactory Object</u>

```
// Configuration

Configuration formats = new Configuration().configure();
SessionFactory factory = configuration.buildSessionFactory();


// Getting properties

ServiceRegistryBuilder registry = new ServiceRegistryBuilder();
registry.applySettings(configuration.getProperties());


// Applying settings

ServiceRegistry register = new StandardServiceRegistryBuilder().applySettings(configuration.getProperties()).build();
```


### <u>Proper Code Example</u>

```
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil_Ex1
{
	private static final SessionFactory sessionFactory = buildSessionFactory();

	private static sessionFactory buildSessionFactory()
	{
		SessionFactory sessionFactory = null;
		
		try
		{
			Configuration configuration = new Configuration();
			configuration.configure("resource/hibernate.cfg.xml");
			sessionFactory = configuration.buildSessionFactory();}
		}

		catch (Exception e)
		{
			e.printStackTable();
		}

		return sessionFactory;
	}

	public static SessionFactory getSessionFactory()
	{
		return sessionFactory;
	}
}
```

- Now we can use `getSessionFactory()` method to access Hibernate session object.

```
Session session = HibernateUtil.getSessionFactory().openSession();
```


### <u>Configuring Mapping Properties</u>

- Actually, the classes & their properties are mapped with tables of the databases, in the configuration file.

```
// <persistent_class_name>.hbm.xml
Employee.hbm.xml
```


### <u>Hibernate Types</u>

- Now we will see SQL equivalent codes for Hibernate/Java types.

| Hibernate Type        | Java Type          | SQL Type              |
| --------------------- | ------------------ | --------------------- |
| integer, long, short  | int, long, short   | NUMERIC, NUMBER, INT  |
| character             | char               | CHAR                  |
| float, double         | float, double      | FLOAT, DOUBLE         |
| boolean               | java.lang.boolean  | BOOLEAN               |
| string                | java.lang.String   | VARCHAR2, VARCHAR     |
| date, time, timestamp | java.util.Date     | DATE, TIME, TIMESTAMP |
| locale                | java.util.Locale   | VARCHAR2, VARCHAR     |
| timezone              | java.util.TimeZone | VARCHAR2, VARCHAR     |