import React from "react";
import {
    Routes,
    Route,
} from "react-router-dom";

import {MovieList, MovieDetail} from '../pages'


const AppRoute = ()=> {
    return (
        <>
            <Routes>

                <Route path="/" >
                    <Route index element={ <MovieList/> } />
                    <Route path="/movie/:id" element={<MovieDetail/>} />
                </Route>

            </Routes>

        </>
    )
}

export {AppRoute}