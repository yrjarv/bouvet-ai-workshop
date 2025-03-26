import React from "react";
import { Link } from "react-router-dom";
import styles from "./Navbar.module.css";
import BouvetLogo from "../../images/BouvetLogo.tsx";

const Navbar = () => {
  const handleLogoClick = () => {
    window.location.reload();
  };

  return (
    <nav className={styles.navbar}>
      <div onClick={handleLogoClick} className={styles.logo}>
        <Link to="/">
          <BouvetLogo />
        </Link>
      </div>

      <Link to="/" className={styles.navLink}>
        Generer oppskrift
      </Link>
      <Link to="/recipes" className={styles.navLink}>
        Mine oppskrifter
      </Link>
    </nav>
  );
};

export default Navbar;
