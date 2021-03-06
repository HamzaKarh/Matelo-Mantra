import {createRouter, createWebHistory} from "vue-router"
import Home from "@/components/Home"
import Musician from "@/components/Musician/Musician";
import Traveler from "@/components/Traveler/Traveler";
import PageNotFound from "@/components/PageNotFound";
import Writer from "@/components/Writer/Writer";
import MusicPage from "@/components/Musician/MusicPage";
import PicAlbumPage from "@/components/Traveler/PicAlbumPage";
import PostPage from "@/components/Writer/PostPage";



const router = createRouter({
  history: createWebHistory(),
  routes: [
        {
            path: "/",
            name: "Home",
            component: Home,
        },
        {
            path: "/music",
            name: "Musician",
            component: Musician,
        },
        {
            path: "/travels",
            name: "Travels",
            component: Traveler,
        },
        {
            path: "/travels/:id",
            name: "Travel_details",
            props: true,
            component: PicAlbumPage,
        },
        {
            path: '/writer',
            name: 'Writer',
            component: Writer,
        },
        {
            path: "/music/:id",
            name: "Music_details",
            props: true,
            component: MusicPage,
        },
        {
            path: "/album_details",
            name: "Album_details",
            component: PicAlbumPage
        },
        {
            path: "/post_details/:id",
            name: "Post_details",
            component: PostPage,
        },
        {
            path: '/:catchAll(.*)*',
            name: "PageNotFound",
            component: PageNotFound,
        },
    ]
})


export default router