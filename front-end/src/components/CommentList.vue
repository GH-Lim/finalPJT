<template>
  <div>
    <div v-if="movie.comments && movie.comments.length">
      <div v-for="(comment, i) in movie.comments" :key="i">
        <p><star-rating :rating="comment.score/2"
          :read-only="true" :increment="0.5" :star-size="15"
          :show-rating="false" :inline="true"></star-rating> {{ comment.score }} | {{comment.user.username}} : {{ comment.content }}</p>
      </div>
    </div>
    <div v-else><h5>평점이 아직 없습니다!</h5></div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: 'CommentList',
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  components: {
    StarRating
  },
  data() {
    return {
    }
  },
  methods: {
  },
}
</script>

<style>

</style>