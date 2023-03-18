import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

// import { Record } from "../views/Record";

/* 
Falta arreglar el view Record para que conecte con el boton de cada tarjeta y 
mostrar la nueva vista con el Detalle de cada Item (personaje o planeta)
*/

export const Card = ({ item, nature }) => {
  const navigate = useNavigate();
  const { store, actions } = useContext(Context);

  return (
    <div className="col">
      <div className="card">
        <img
          src={`https://starwars-visualguide.com/assets/img/${nature}/${item.result.uid}.jpg`}
          className="card-img-top"
          alt="..."
        />
        <div className="card-body">
          <h5 className="card-title">{item.result.properties.name}</h5>
          {nature == "characters" ? (
            <>
              <p>Gender: {item.result.properties.gender}</p>
              <p>Hair Color: {item.result.properties.hair_color}</p>
              <p>Eyes: {item.result.properties.eye_color}</p>
            </>
          ) : (
            <>
              <p>Population: {item.result.properties.population}</p>
              <p>Terrain: {item.result.properties.terrain}</p>
            </>
          )}
            <div className="d-flex justify-content-between">
              <button
                onClick={() => navigate(`record/${nature}/${item.result.uid}`)}
                className="btn btn-outline-primary"
              >
                Learn more!
              </button>

              { store.favorites.includes(item.result.properties.name) ? (
                <button
                  className="btn btn-outline-warning"
                  onClick={() => actions.deleteFavorite(item.result.properties.name)}
                >
                  💛
                  </button>
                ) : (
                  <button
                  className="btn btn-outline-warning"
                  onClick={() => actions.setFavorite(item.result.properties.name)}
                >
                  💛
                  </button>
                  )}
            </div>
        </div>
      </div>
    </div>
  );
};