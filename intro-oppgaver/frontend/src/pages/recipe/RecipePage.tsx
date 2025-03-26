import RecipesContext from "../../context/RecipesContext.tsx";
import Markdown from "react-markdown";
import styles from "./RecipePage.module.css";
import { useContext } from "react";
import { useParams } from "react-router-dom";
import { NotFound } from "../../components/NotFound/NotFound.tsx";

export function RecipePage() {
  const { id } = useParams();
  const { recipeList } = useContext(RecipesContext);
  const recipe = recipeList?.find((r) => r.id == id);

  if (!recipe) {
    return <NotFound text={"Oops 🙅‍♂️🍳 No recipe found for ID: " + id} />;
  }

  return (
    <div className={styles.recipe_container}>
      <img
        className={styles.recipe_image}
        src={recipe.imageUrl}
        alt="Recipe image"
      />

      <section>
        <div className={styles.recipe_text}>
          <h3>Ingredients</h3>
          <p className={styles.recipe_ingredients}>
            {recipe.ingredients.join(", ")}
          </p>
        </div>

        <div className={styles.recipe_text}>
          <Markdown>{recipe.recipeText}</Markdown>
        </div>
      </section>
    </div>
  );
}
