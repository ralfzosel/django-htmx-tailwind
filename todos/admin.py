from compressor.filters import CompilerFilter


class PostCSSFilter(CompilerFilter):
    command = 'npx postcss'
