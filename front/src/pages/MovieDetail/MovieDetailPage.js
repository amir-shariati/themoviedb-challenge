import React, {useState, useEffect} from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

const MovieDetail = (props) => {
    const [movie, setMovie] = useState(null);

    const { id } = useParams()
    const navigate = useNavigate();

    useEffect(() => {
        const fetchMovieDetail = async () => {
            try {
                const response = await axios.get(`http://0.0.0.0:8000/api/movie/${id}`);
                setMovie(response.data);
            } catch (error) {
                console.error('Error fetching movie detail:', error);
            }
        };

        fetchMovieDetail();

    }, [id]);


    const handlerOnClick = () => {
        console.log('back clicked')
        navigate('/');
    }

    if (!movie) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{movie.title}</h1>
            <img src={`http://image.tmdb.org/t/p/original${movie.poster_path}`} alt={movie.title}/>
            <p>Release Date: {movie.release_date}</p>
            <p>Overview: {movie.overview}</p>
            <button onClick={handlerOnClick}>Back</button>
        </div>
    );
};

export {MovieDetail}