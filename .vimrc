" ced's vimrc

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

syntax enable
filetype on

set hidden
set history=100
set number
set hlsearch
set mouse=a
set ruler
set cursorline
set incsearch
set noshowmode

set colorcolumn=81
highlight colorcolumn ctermbg=6

set wildmenu
set relativenumber
set clipboard=unnamed
set backspace=indent,eol,start
set scrolloff=5
set background=dark

set laststatus=2

autocmd FileType make set noexpandtab
autocmd FileType tex set colorcolumn=

noremap <F2> :bp<CR>
noremap <F3> :bn<CR>
nmap    <F1> <nop> 

if exists('+termguicolors') && ($TERM == "st-256color" || $TERM == "tmux-256color" || $TERM == "xterm-256color")
    let &t_8f = "\e[38:2:%lu:%lu:%lum"
    let &t_8b = "\e[48:2:%lu:%lu:%lum"
    let &t_RF = "\e]10;?\e\\"
    let &t_RB = "\e]11;?\e\\"
    set termguicolors
endif
set termguicolors
set background=dark
colorscheme rosepine

hi Normal guibg=NONE
