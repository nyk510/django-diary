<template>
  <v-layout
    row
    row-wrap>
    <v-flex
      v-for="item in articles"
      :key="item.id"
      xs12
      sm8
      md6>
      <v-card
        :to="'blog/' + item.id">
        <v-card-title>{{ item.title }}</v-card-title>
        <v-card-text>{{ item.body }}</v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  async asyncData ({ app }) {
    const articles = await app.$axios.$get('articles/')
    return {
      articles: articles
    }
  }
}
</script>
