# $\fbox{Chapter 4: ANGULAR}$





## **Topic - 1: Basic Concepts**

### <u>Introduction</u>

- Angular is open-source.


### <u>Key Features</u>

#### Component-based architecture:

- **<u>Components</u>:** Reusable parts of code that encapsulate more complex parts.
- This helps in easier maintenance & scaling.

#### Two-way data binding:

- Two-way data binding means that changes in an Angular application UI is reflected in its data model & vice-versa.
- **<u>Data model</u>:** Internal class objects that a library/template use.
- So, Angular automatically syncs data between UI & model.

#### Dependency injection:

- Dependency injection allows to easily integrate dependencies (injecting) into other codes.
- It also gives facility to test your code.

#### Directives:

- **<u>Directives</u>:** Markers on DOM elements that requires it to behave in a particular way.
- Some built-in directives in Angular are `ngIf`, `ngFor` & `ngModel`.
- These models enhance the functioning of HTML elements.

#### Services:

- Services are used to share code across channels connecting all application components.
- This is enhanced by Angular's dependency injection.

#### Routing:

- Angular provides a great routing system.
- Routing allows a user to navigate through web application without reloading the page.
- This allows building SPAs with multiple views.

#### Forms:

- Angular supports creation & management of forms.
- It supports both template-driven & reactive forms.

#### TypeScript:

- Angular is written using TypeScript which is statically typed form of JavaScript.


### <u>Installation Steps</u>

1. Install **node.js**.
2. Install **npm**.
3. Install Angular.

```sh
npm install -g @abgular/cli
```

4. Set up an Angular project.

```sh
ng new your-angular-app
```

5. Navigate to directory.

```sh
cd your-angular-app
```

6. Serve the application through development server.

```sh
ng serve
```

7. Open browser at link `http://localhost:4200/`.


### <u>Other Angular Commands</u>

#### Generating new component:

```sh
ng generate component <component-name>
```

#### Including routing:

- Add the flag `--routing`.

```sh
ng new my-new-app --routing
```



## **Topic - 2: Components In Angular**

### <u>Introduction</u>

- Each Angular component is a self-contained unit.
- These components offer modularity, reusability & isolation.


### <u>Generating Component</u>

#### Step 1:

```sh
ng generate component first-task
```

$$OR$$

```sh
ng g c first-task
```

- This creates following components.

![Created components](./media/image8.png)
