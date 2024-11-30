# <u>Chapter 3</u>: JAVA SERVER PAGE





## **Topic – 1: Need Of JSP**

### <u>Java Server Page (JSP)</u>

- **<u>JSP</u>:** Provides template to create dynamic HTML websites using Java.
- **<u>JSP containers</u>:** Converts JSP codes into equivalent Servlet codes.
- We can say that JSP provides GUI to users for interactions.
- JSP has ability to embed HTML, XHTML, XML, JSTL etc.
- And it is more flexible than Servlet.


### <u>JSP Processing</u>

- JSP is processed on server only.



## **Topic – 2: Advantages Of JSP**

- **Easy maintenance**, as it separates codes for business logic & way to present website.
- **Servlet’s extension**.
- **Requires less coding**, as custom tags can be embedded.
- **Fast development**, as modifying a JSP page has immediate effects, we don’t need to re-deploy.
- **Easy integration**, as we can embed many codes.



## **Topic – 3: Difference Between JSP & Servlet**

| JSP | Servlet |
|----|----|
| Server-side technology. | Java class program. |
| Easy maintenance, separating codes for business & web presentation. | Difficult to maintain having no separation among codes. |
| Change in code doesn’t require re-deployment. | Change in code requires re-deployment. |
| Can use custom tags. | Can’t use custom tags. |
| Accepts only HTTP requests. | Accepts any kind of requests. |
| Can import packages anywhere in the code. | Packages need to imported at top of Servlet codes. |
| Automatic session management. | Manual session management. |
| Model view controller gives viewer/user experience. | Model view controller gives controller experience. |



## **Topic – 4: JSP Lifecycle**

### <u>Lifecycle Diagram</u>

![JSP Lifecycle](Enterprise%20Programming/ByteXL%20{D}/media/image1.png)


### <u>Steps Involved In Lifecycle</u>

- Translation
- Compilation
- Servlet class loading
- Servlet instance creation
- Servlet initialization
- Servicing client requests
- Servlet destruction



## **Topic – 5: JSP Scripting Elements**

### <u>JSP Tags</u>

- JSP scriptlet tag
- JSP declarations tag
- JSP directives tag
- JSP expression tag


### <u>Scriptlet Tags</u>

- **<u>Scriptlet</u>:** Java statements embedded in a HTML page.
- But we use it to just declare variables.
- Enclosed between `<%` and `%>`.
- JSP transfers these to `jspService()` method for generating Servlet.

```
<% int count = 0; %>

<body>
  Page count is <% out.println(++count); %>
</body>
```


### <u>JSP Declarations</u>

- Used to declare method or variables in HTML pages.
- Enclosed between `<!%` and `%>`.
- Is not passed to `_jspService()` method.

```
<%! String name = "Gourav"; %>
```


### <u>JSP Directives</u>

- Written at top of JSP files.
- Used for global definition like importing packages or declaring
  errors.
- Contains special processing information for JSP container.
- Enclosed between `<@%` and `%>`.
- Usable attributes for directives - `import`, `language`, `extends`, `session`,
  `isThreadSafe`, `isErrorPage`, `errorPage`, `contentType`, `autoFlush`, `Buffer`
  etc.

```
<%@ include file="myfile.jsp" %>
<%@ taglib uri="<http://someWebsite>" prefix="demotag" %>
```


### <u>Types Of Tags</u>

- Core tags
- Formatting tags
- SQL tags
- XML tags
- JSTL functions


### <u>JSP Expressions</u>

- Evaluates the expression stored in it.
- Required when user makes HTTP request.

```
<%= new String("Hello World").toUpperCase() %>  
<%= num1 + num2 + num3 %>
```


### <u>JSP Comments</u>

```
<%-- JSP comment %>
<% /** multiline comment **/%>
<!-- HTML comment -->
```


### <u> JSP Implicit Objects </u>

- **<u>Implicit objects</u>:** Built-in objects a developer can use on each page, provided by JSP container.
- These can also be accessed using **JavaBeans** & **Servlets**.

#### Objects we can use:

- **request -** Makes request using `HttpServletRequest` object.
- **response -**  Takes response from `HttpServletResponse` object.
- **out -** Displays output from request & response objects, using `JspWriter` object.
- **session -** Represents session for a given request using `HttpSession` object.
- **application -** Shares our application configuration using `ServletContext` object.
- **config -** Sets configuration using `ServletConfig` object.
- **page -** Represent current instance of JSP page, i.e. current instance of generated Servlet. Uses `java.lang.Object`.
- **pageContext -** Adds, removes or modifies configuration/attributes using `javax.servlet.jsp.PageContext` object.
- **exception -** Throws exceptions using `javax.servlet.jsp.JspException` object.



## **Topic - 6: Key Implicit Objects Methods**

### <u>JSP config</u>

```
String getInitParameter(String name)
Enumeration getInitParameterNames
ServletContext getServletContext()
String getServletName()
```


### <u>JSP out</u>

```
void print()
void println()
void newline()
void clear()
clearBuffer
void flush()
void isAutoFlush()
int getBufferSize()
```


### <u>JSP pageContext</u>

```
void setAttribute(String AttributeName, Object AttributeValue, int Scope)
Object getAttribute(String AttributeName, int Scope)
void removeAttribute(String AttributeName, int Scope)
Object findAttribute(String AttributeName)
```



## **Topic - 7: JSP Scripting Elements (Contd.)**

### <u>JSP Exception</u>

- Uses `java.lang.Throwable` object.
- But a JSP page must have an `isErrorPage` to be able to use it.

```
<%@ page errorPage="exception.jsp" %>

<%
	/*
	Java codes...
	Will throw error if caught.
	*/
%>
```


### <u>JSP Action</u>

- Controls behavior of Servlet engine using XML syntax.
- It also allows dynamic insertion of a JSP file.

#### Uses following code format:

```
<jsp:actionname attribute="">
```

#### JSP action tags:

```
<jsp:forward>
<jsp:include>
<jsp:plugin>
<jsp:param>
<jsp:useBean>
<jsp:getProperty>
<jsp:setProperty>
<jsp:body>
<jsp:attribute>
<jsp:text>
```

#### JSP action tags examples:

```
<jsp:param name="name" value="value"/>
<jsp:setProperty name="name" property="property"/>
```


### <u>Expression Language</u>

- It simplifies accessing data using JSP objects with arithmetic, relational & logical operators.
- It also uses conditional statements & loops.

```
${1<2}, ${1+2+3}, ${param.emailid}
```



## **Topic - 8: Java Server Pages Standard Tag Library (JSTL)

### <u>Introduction</u>

- Collection of standard & custom JSP tags for helping smoother development.
- It is like `<string.h>` in C for example.

#### Types of JSTL tags:

- Core tags
- Custom tags


### <u>Core Tags</u>

- Iteration
- Conditional logic
- Catch exception
- URL forward
- Redirect

#### Example 1:

```
<c:catch var="myException">
	<% int num = 10/0; %>
</c:catch>
```

#### Example 2:

```
<c:if test="${count == 100}"/>
	<c:out value="The count is 100"/>
</c:if>
```


### <u>Custom Tags</u>

- **<u>Tag handler</u>:** Is is the object JSP container uses when using custom tags.
- To create a custom tag, we need to extend `SimpleTagSupport` object & override `doTag()` method.
- We create TLD files to map our custom tag details there.

#### Making custom tag:

```
<taglib>
	<tlib-version> 1.0 </tlib-version>
	<jsp-version> 2.0 </jsp-version>
	
	<tag>
		<name> myTag </name>
		<tag-class> demotest.myTag </tag-class>
		<body-content> empty </body-content>
	</tag>
</taglib>
```

- Notice that TLD is just used to provide information about our custom tag.

#### Making a tag handler:

- An example for a tag handler file will be as below as `myTag.java`.

```
package demotest;
import javax.servlet.jsp.tagext.*;
import javax.servlet.jsp.*;
import java.io.*;

public class myTag extends SimpleTagSupport
{
	public void doTag() throws JspException, IOException
	{
		JspWriter out = getJspContext().getOut();
		out.println("This is myTag!");
	}
}
```

#### Executing the tag code:

```
<%@ taglib prefix="ex" uri="WEB-INF/custom.tld" %>

<body>
	<ex:myTag/>
</body>
```

- `ex` above means **execute**.

---
