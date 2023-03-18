import React, {useContext} from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
// import { Favorites } from "./Favorites";

/* Falta arreglar el compoennte Favorites para agregar cada item a los favoritos del dropdown*/

export const Navbar = () => {
	const {store, actions } = useContext(Context);
	const {favorites} = store;

	return (
		<div className="container">
			<nav className="navbar navbar-light bg-light mb-3">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">
						<img src="https://www.iconspng.com/uploads/star-wars-logo.png" width="100" height="80" />
					</span>
				</Link>
				<div className="ml-auto">
					<Link to="/">
					<div className="btn-group">
						<button type="button" className="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
							Favorites <span className="badge bg-secondary">{store.favorites.length}</span>
						</button>
						<ul className="dropdown-menu">
							{store.favorites.length == 0 
							? "No items yet" 
							: favorites.map((item) => {
								return (
									<li>
										<a onClick={ () => actions.deleteFavorite(item) } className="dropdown-item">
											{item} ❌
										</a>
									</li>
								)
							})}
						</ul>
					</div>
					</Link>
				</div>
			</nav>
		</div>
	);
};