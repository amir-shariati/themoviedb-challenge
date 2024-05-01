import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';


const MovieList = () => {

    const [movies, setMovies] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [nextPage, setNextPage] = useState(null);
    const [prevPage, setPrevPage] = useState(null);


    useEffect(() => {
        fetchMovies();
    }, []);


    const fetchMovies = async (url) => {
        try {
            const response = await axios.get(url || 'http://0.0.0.0:8000/api/movie');
            setMovies(response.data.results);
            setNextPage(response.data.next);
            setPrevPage(response.data.previous);
        } catch (error) {
            console.error('Error fetching movies:', error);
        }
    };

    const handleNextPage = () => {
        if (nextPage) {
            fetchMovies(nextPage);
        }
    };

    const handlePrevPage = () => {
        if (prevPage) {
            fetchMovies(prevPage);
        }
    };



    const handleSearch = async () => {
        try {
            const response = await axios.get(`http://0.0.0.0:8000/api/movie?search=${searchTerm}`);
            setMovies(response.data.results);
            setNextPage(response.data.next);
            setPrevPage(response.data.previous);
        } catch (error) {
            console.error('Error searching movies:', error);
        }
    };


    return (
        <div>
            <input type="text" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
            <button onClick={handleSearch}>Search</button>
            <button onClick={handlePrevPage} disabled={!prevPage}>Previous</button>
            <button onClick={handleNextPage} disabled={!nextPage}>Next</button>
            <ul>
                {movies.map((movie) => (

                    <li key={movie.id}>
                        <Link to={`/movie/${movie.id}`}>
                            <p>{movie.title}</p>
                            <img src={`http://image.tmdb.org/t/p/w500${movie.poster_path}`} alt={movie.title}/>
                        </Link>
                    </li>

                ))}
            </ul>
        </div>
    );
};

export {MovieList}