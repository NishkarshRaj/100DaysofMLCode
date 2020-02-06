# K-Nearest Neighbors classification

**Intution:** We have a data set divided into different categories, and when a new tuple is added to it, we have to classify in which category does the new tuple belongs to.

## KNN Algorithm

**Step 1:** Decide the value of parameter K. Generally 5 is chosen as the default value.

**Step 2:** Find the K nearest neighbors of the new element based on distance (Eucledian Geometry is preferred but any distance can be chosen like Manhattan)

**Step 3:** Count the number selected neighbors in each category

**Step 4:** Assign the new tuple to the category having maximum neighbors.

## Eucledian Distance

The geometric distance between two points P1(x1,y1) and P2(x2,y2) can be found by the formulae `sqrt((x1-x2)**2 + (y1-y2)**2)`
