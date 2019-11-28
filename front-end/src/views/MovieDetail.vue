<template>
  <b-container fluid class="p-4 bg-gradient-dark">
    <b-img :src="movie.backgroundImage" fluid-grow alt="" class="mb-3"/>
    <div class="row">
      <div class="col-2">
        <b-img thumbnail :src="movie.image" fluid :width="200" class="mb-3"/>
        <span class="btn btn-outline-danger" @click="clickLike">
          <h2 class="d-inline"><span v-if="liked">♥</span><span v-else>♡</span></h2>
          <span>{{ count }}명이 좋아합니다.</span>
          <!-- <span v-if="liked">찜하기 취소</span><span v-else>찜하기</span> -->
        </span>
      </div>
      <div class="col-5">
        <h5>{{ movie.title }}</h5>
        <h6>개봉일: {{ movie.openDt }} <span class="badge badge-info">{{ movie.score }}</span></h6>
        <span>{{ movie.description }}</span>
      </div>
      <div class="col-5">
        <CommentBox :movie="movie" :comments="comments" @createComment="createComment"/>
      </div>
    </div>
  </b-container>
</template>

<script>
import axios from "axios"
import { mapGetters } from 'vuex'
import CommentBox from '@/components/CommentBox'
// import MoviePoster from "./MoviePoster"

export default {
  name: "MovieDetail",
  props: {},
  components: {
    CommentBox,
    // MoviePoster,
  },
  data() {
    return {
      user: {},
      movie: {},
      comments: [],
      liked: false,
      count: 0,
    }
  },
  methods: {
    createComment(data) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const headers = this.options
      axios.post(`${SERVER_IP}/api/v1/movies/${this.movie.id}/comment/`, data, headers)
       .then(response => {
         alert('작성되었습니다.')
         console.log(response.data)
         this.comments.push(response.data)
       })
       .catch(error => {
         console.error(error)
       })
      this.$nextTicl(() => {
        this.comments = this.comments
      })
    },
    clickLike() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const headers = this.options
      axios.get(`${SERVER_IP}/api/v1/like/${this.movie.id}/`, headers)
        .then(response => {
          this.liked = response.data.liked
          this.count = response.data.count
        })
        .catch(error => {
          console.error(error)
        })
    },

  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ]),
  },
  mounted() {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    const headers = this.options
    axios.get(`${SERVER_IP}/api/v1/movies/${this.$route.params.id}/`, headers)
      .then(response => {
        this.movie = response.data
        this.comments = this.movie.comments
        this.count = this.movie.like_users.length
        axios.get(`${SERVER_IP}/api/v1/userdetaildb/${this.userId}/`, headers)
          .then(user => {
            for (const likeMovie of user.data.like_movies) {
              if (likeMovie.id === this.movie.id) {
                this.liked = true
                break
              }
            }
          })
      })
      .catch(error => {
        console.error(error)
      })
  },
  watch: {
  }
}
</script>

<style>
  /* .thumbnail {
    display: inline;
  } */
  .detail {
    display: inline;
  }
</style>