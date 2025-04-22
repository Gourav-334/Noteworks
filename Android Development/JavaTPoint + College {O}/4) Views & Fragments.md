# $\fbox{Chapter 4: VIEWS \& FRAGMENTS}$





## **Topic - 1: `GridView`**

### <u>Introduction</u>

- **<u>GridView</u>:** 2D scrolling layout
- Grid items are inserted using `ListAdapter`.
- Doesn't require help from `ScrollView` class to scroll.
- Has inbuilt scrolling feature.


### <u>Attributes</u>

- `id` - Uniquely identified a `GridView`.
- `numColumns` - Total columns (integer or `auto_fit`).
- `horizontalSpacing` - Space between columns (in `px`, `dp` or `sp`).
- `verticalSpacing`
- `columnWidth`

>**<u>NOTE</u>:**
>1. `px` is pixel.
>2. `dp` is density pixel.
>3. `sp` is scale independent pixel.


### <u>Adapter Class</u>

- Adapter is responsible for bridging UI elements & data they represent.
- `GridView` & `ListView` are subclasses of `Adapter`.

#### Types of adapters:

1. **<u>Array adapter</u>:** For array-like data as input.
2. **<u>Base adapter</u>:** Array adapter with modifications.
3. **<u>Custom array adapter</u>:** Completely custom adapter.



## **Topic - 2: `ListView`**

### <u>Introdcution</u>

- `ListView` arranges items in form of a scrollable list.
- Doesn't require help from `ScrollView` class to scroll.
- Has inbuilt scrolling feature.


### <u>Attributes</u>

- `id`
- `divider` - Coloured line between each list item.
- `dividerHeight` - Height of the `divider`.
- `listSelector` - The colour or image that appears when a list item is chosen.

>**<u>NOTE</u>:**
>`ListView` has the same set of adapters as `GridView`.



## **Topic - 3: `ScrollView`**

### <u>Types Of Scrolling</u>

- Horizontal `ScrollView`
- Vertical `scrollView`


### <u>Attributes</u>

- `id`
- `scrollbars`



## **Topic - 4: `RecyclerView`**

- A dynamic approach to view elements efficiently.
- We set the views & properties at first.
- Then the required elements are created dynamically when required.
- The recycler reuses/recycles the existing views for upcoming elements instead of destroying them.
- This reduces a lot of power consumption.



## **Topic - 5: `CardView`**

### <u>Introduction</u>

- Used to display elements like cards.
- Elements have rounded corners.
- Also they can be displayed over each other.
- `CardView` is extension of `FrameLayout`.


### <u>Attributes</u>

- `cardCornerRadius`
- `cardBackgroundColor`
- `cardElevation` - Yes, its the drop shadow effect.
- `cardMaxElevation`
- `UseCompactPadding` - Space around the elevation.



## **Topic - 6: Fragment & Lifecycle**

### <u>Introduction</u>

- **<u>Fragment</u>:** Reusable portion of an app's UI.
- Their lifecycle relies on other activities, they don't handle themselves.


### <u>Lifecycle Stages</u>

1. `onCreate()`
2. `onStart()`
3. `onResume()`
4. `onPause()`
5. `onStop()`
6. `onDestroy()`

>**<u>NOTE</u>:**
>Lifecycle of fragments can't move upward, it only goes down.

---
