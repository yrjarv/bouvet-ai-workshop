import RecipesContext from "../../context/RecipesContext";
import { useNavigate } from "react-router-dom";
import { useContext, useEffect } from "react";
import { useUserId } from "../../hooks/useUserId.ts";
import styles from "./RecipesPage.module.css";
import { NotFound } from "../../components/NotFound/NotFound.tsx";

export function RecipeListPage() {
  const navigate = useNavigate();
  const { recipeList, setRecipes } = useContext(RecipesContext);
  const userId = useUserId();

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await fetch(
          "http://127.0.0.1:5000/recipes?user_id=" + userId
        );

        if (!response.ok) {
          const errorJson = await response.json();
          console.error(
            "fetchRecipes failed\n",
            "Status code: " + response.status + "\n",
            "Error message: " + errorJson.error + "\n"
          );
          return;
        }

        const data = await response.json();
        setRecipes(data);
      } catch (error) {
        console.error("Error fetching recipes:", error);
      }
    };

    fetchRecipes();
  }, [setRecipes, userId]);

  if (!recipeList || recipeList.length == 0) {
    return <NotFound text={"You have no recipes"} />;
  }

  return (
    <div className={styles.container}>
      {recipeList.map((recipe) => (
        <div
          key={recipe.id}
          className={styles.recipeCard}
          onClick={() => {
            navigate("/recipes/" + recipe.id);
          }}
        >
          <img
            className={styles.recipeImage}
            src={recipe.imageUrl}
            alt="Recipe"
          />
          <div className={styles.recipeIngredients}>
            {recipe.ingredients.join(", ")}
          </div>
          <div className={styles.recipeText}>{recipe.recipeText}</div>
        </div>
      ))}
    </div>
  );
}
