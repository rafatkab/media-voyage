export interface movieObj {
    adult: boolean;
    backdrop_path: string;
    genre_ids: number[];
    id: number;
    original_language: string;
    original_title: string;
    overview: string;
    popularity: number;
    poster_path: string;
    release_date: string;
    title: string;
    video: boolean;
    vote_average: number;
    vote_count: number;
}

export interface movieDetails {
    adult: boolean,
    backdrop_path: string,
    belongs_to_collection: {backdrop_path: string, id: number, name: string, poster_path: string}
    budget: number
    genres: {id: number, name: string}[]
    homepage: string
    id: string
    imdb_id: string
    original_language: string
    original_title: string
    overview: string
    popularity: number
    poster_path: string
    production_companies: {id: number, logo_path: string, name: string, origin_country: string}[]
    production_countries: {iso_3166_1: string, name: string}[]
    release_date: string
    revenue: number
    runtime: number
    spoken_languages: {english_name: string, iso_639_1: string, name: string}[]
    status: string
    tagline: string
    title: string
    video: boolean
    vote_average: number
    vote_count: number
}

export interface movieRating {
    id: number;
    account_id: number;
    movie_id: number;
    poster_path: string;
    rating: number;
    title: string;
}

export interface RegisterData {
    birthDate: string;
    userName: string;
    pass: string;
    confirmPass: string;
    email: string;
  };

  export interface LoginData {
    userName: string;
    pass: string;
  }

export interface Account {
    birth_date: string;
    email: string;
    id: number;
    password: string;
    username: string;
};