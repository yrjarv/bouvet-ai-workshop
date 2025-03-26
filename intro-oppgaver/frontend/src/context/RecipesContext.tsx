import React from "react";
import Recipe from "../model/Recipe";

const RecipesContext = React.createContext<{
  recipeList: Recipe[];
  setRecipes: (recipes: Recipe[]) => void;
}>({
  recipeList: [],
  setRecipes: () => {},
});

export default RecipesContext;
