<template>
  <div>
    <div v-if="byGenre">
      <p>{{ byGenre }} 장르의 검색 결과입니다.</p>
    </div>
    <div v-if="movies && movies.length">
      <MovieList :movies="movies" :genres="genreSelect.options" class="container mx-auto" />
    </div>
    <div v-else>
      <p>검색결과가 없습니다.</p>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
  name: 'Search',
  components: {
    MovieList,
  },
  props: {
    movies: {
      type: Array
    },
    byGenre: {
      type: String
    },
    genreSelect: {
      type: Object
    }
  }
}
</script>

<style>

</style>