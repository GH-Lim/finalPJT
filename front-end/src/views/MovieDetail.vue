<template>
  <b-container fluid class="p-4 bg-gradient-dark">
    <b-img :src="movie.backgroundImage" fluid-grow alt="" class="mb-3"/>
    <div class="row">
      <div class="col-2">
        <b-img thumbnail :src="movie.image" fluid :width="200" class="mb-3"/>
        <span class="btn btn-outline-danger">
          <h2 class="d-inline"><span v-if="liked">♥</span><span v-else>♡</span></h2>
          <span v-if="liked">찜하기 취소</span><span v-else>찜하기</span>
        </span>
      </div>
      <div class="col-5">
        <h5>{{ movie.title }}</h5>
        <h6>개봉일: {{ movie.openDt }} <span class="badge badge-info">{{ movie.score }}</span></h6>
        <span>{{ movie.description }}</span>
      </div>
      <div class="col-5">
        <CommentBox :movie="movie" @createComment="createComment"/>
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
      liked: null,
      count: 0,
    }
  },
  methods: {
    createComment(data) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const headers = this.options
      axios.post(`${SERVER_IP}/api/v1/movies/${this.movie.id}/comment/`, data, headers)
       .then(() => {
         alert('작성되었습니다.')
       })
       .catch(error => {
         console.error(error)
       })
    },
    clickLike() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const headers = this.options
      axios.get(`${SERVER_IP}/api/v1/like/${this.movie.id}/`, headers)
        .then(response => {
          this.liked = response.liked
          this.count = response.count
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  mounted() {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    const headers = this.options.headers
    axios.get(`${SERVER_IP}/api/v1/movies/${this.$route.params.id}/`, {headers: headers})
      .then(response => {
        this.movie = response.data
        this.comments = this.movie.comments
      })
      .catch(error => {
        console.error(error)
      })
  },
  watch: {
    isLoggedIn() {

    }
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