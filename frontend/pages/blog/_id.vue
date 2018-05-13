<template>
  <v-layout column>
    <v-flex v-if="article">
      <v-subheader>{{ article.title }}</v-subheader>
      <v-card>
        <v-card-media :src="article.main_image"/>
        <v-card-text>
          {{ article.body }}
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data () {
    return {
      article: null
    }
  },
  async asyncData ({ app, params }) {
    const res = await app.$axios.$get('/articles/' + params.id + '/')
    console.log(res)
    return {
      article: res
    }
  }
}
</script>
