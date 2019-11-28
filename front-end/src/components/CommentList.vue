<template>
  <div>
    <h4>한줄평</h4>
    <div v-if="comments && comments.length">
      <div v-for="(comment, i) in comments" :key="i">
        <star-rating :rating="comment.score/2"
          :read-only="true" :increment="0.5" :star-size="15"
          :show-rating="false" :inline="true"></star-rating>
          <span>{{ comment.score }} | {{ comment.user["username"] }} : {{ comment.content }}</span>
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
    },
    comments: {
      type: Array,
    }
  },
  components: {
    StarRating
  },
  data() {
    return {
    }
  },
}
</script>

<style>

</style>